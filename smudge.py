import click
import os
import datetime
from pathlib import Path
import subprocess


@click.group()
def cli():
	"""Smudge: For better blotting from the command line!"""
	pass

@cli.command()
def publish():
	"""Publish to your blot"""
	# Should add, commit and push to blot

	blotpath = os.getenv("BLOTDIR")

	if blotpath:
		cwd = os.getcwd()

		expanded_blotpath = os.path.expanduser(blotpath)

		os.chdir(expanded_blotpath)

		subprocess.call(["git", "add", "{}".format(expanded_blotpath)])

		now = datetime.datetime.today()

		subprocess.call(["git", "commit", "-m", "New publish {}-{}".format(str(now.day) + str(now.month) + str(now.year), str(now.second) + str(now.minute) + str(now.hour))])
		subprocess.call(["git", "push"])

		os.chdir(cwd)
	else:
		no_blotpath()


@cli.command()
@click.option('--publish', '-p', is_flag=True, help="Publish immediately")
@click.option('--write', '-w', default='', help="Don't open a text editor - pass in a string for content")
@click.option('--filetype', '-f', default='txt', help="The file extention (i.e. md, txt) defaults to txt")
@click.pass_context
def micro(ctx, publish, write, filetype):
	"""Create a micro post"""
	# Create a new file in the micro directory
	now = datetime.datetime.today()
	filename = "{}-{}.{}".format(str(now.day) + str(now.month) + str(now.year), str(now.second) + str(now.minute) + str(now.hour) ,filetype)

	#blotpath = Path.home() / 'Rambling' / 'hill'

	blotpath = os.getenv("BLOTDIR")

	if blotpath:
		micropath = Path(blotpath) / 'micro'
		micropath = os.path.expanduser(micropath)
		#click.echo(micropath)

		# should check if the micropath exists
		if not Path(micropath).exists():
			click.echo("A micro directory does not exist. Creating one now...")
			p = Path(micropath)
			p.mkdir()

		if write:
			with open(str(micropath) + '/' + filename, mode='w') as f:
				f.write(write)
		else:
			#click.echo("Open {}!".format(os.getenv("EDITOR"))
			subprocess.call(["nano", "{}/{}".format(micropath, filename)])

		if publish:
			ctx.invoke(publish)
	else:
		no_blotpath()

def no_blotpath():
	click.echo(click.style("\nYou need to set your blot directory!", fg='red', bold=True))
	click.echo("Add: " + click.style("export BLOTDIR='~/path/to/blot'", fg='green') + " to your ~/.bashrc or ~/.zshrc")
	click.echo("Then run: " + click.style("source ~/.bashrc", fg='green') + " (or ~/.zshrc)\n")
