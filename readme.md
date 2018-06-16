# Smudge

> A Blot CLI

Smudge is a tiny CLI to let you easily publish to your [blot](http://blot.im) blog without going through the process of commiting to a git repo.

It also makes writing micro posts a bit more efficient.

### Set Up

Add something like:
```bash
export BLOTDIR='~/path/to/blot'
```
to `~/.bashrc` or `~/.zshrc`

then run

`source ~/.bashrc` (or `~/.zshrc`)

### Usage

Publish your blot blog:

```
$ smudge publish
```

Create a new micro post:
```
$ smudge micro
```

Create a new micro post with a string:

```
$ smudge micro -w "This is a quick micropost"
```

Immediately publish your micro post

```
$ smudge micro -p
```


### Disclaimer

I have no idea what I'm doing. :)

Feel free to add what you want and submit a pr.
