# MatthewGilbert
This is the source code for the blog hosted
[here](http://www.matthewdgilbert.com/)

## Requirements
* `pelican==3.6.3` should be used. There is an issue with `3.7` not properly
rendering the colors
* using a fork of [bootstrap-3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
to avoid having a banner title.

## Notes
* To render `ipynb` files run `jupyter nbconvert --to markdown MYFILE.ipynb`
    * The `.md` files need the following added to the top
    > title:
    * The language markups also need to be changed from "\`\`\`python" to "\`\`\`language-python"

* [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) used to be
used to render ipynb files, this is an alternative option
* To recursively clone with all submodules use `git clone --recursive git@github.com:matthewgilbert/blog.git`
