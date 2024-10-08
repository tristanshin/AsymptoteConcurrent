# Asymptote Concurrent

A simple script to compile [Asymptote](https://asymptote.sourceforge.io/) concurrently, using Python's multiprocessing package. By default, the script uses half of your available threads but can be told to use a different number via an argument.

**WARNING**: If you overload the script, it may hang unexpectedly. Some ways of doing this include running the script multiple times at the same time or in a row, compiling too many Asymptote files (usually around 100), or having many files require 3D graphics rendering (some issues arise when multiple threads attempt to use Asymptote's 3D graphics renderer at the same time). I am still looking into ways to mitigate these issues.

I found that the script hangs much more often on MacOS than on Windows. I also found that Asymptote compilation may just be a lot faster on Linux/Unix than Windows too, so this script is probably only useful on Windows.

## Install

The main thing you need is the asyc.py file and a way to run it with command line tools. On Windows, clone this repository and put the directory in your PATH. On Linux/Unix, as mentioned above, this script is probably not actually useful (and may be more likely to hang). But if you want to use it still, clone the repository and add a custom command to your ~/.bashrc or ~/.zshrc (or similar):
```bash
function asyc() {
	python3 ${DIRECTORY_OF_REPO}/asyc.py "$@"
}
```
where you replace ```{DIRECTORY_OF_REPO}``` with the directory that you cloned this to. For example, if I cloned this repository to my Documents folder, the path above would be ```$~/Users/USERNAME/Documents/AsymptoteConcurrent/asyc.py```.

## Usage

- ```asyc```: Compiles all .asy files in the current directory.
- ```asyc filename```: Compiles all .asy files generated by a LaTeX file called ```filename.tex```; equivalently compiles everything matching the regular expression ```filename-[0-9]+\.asy```.
- ```asyc .\filename.tex```: Same as above; the command attempts to strip off the leading ```.\``` as well as any extensions, allowing for easier tab completion.
- ```asyc --processes=4``` or ```asyc -p=4```: Uses 4 processes instead of the default.

### TeXstudio

To use asyc instead of a linear Asymptote compilation in TeXstudio, change ```Options > Configure TeXstudio > Commands > Asymptote``` to ```asyc.bat %```. If you want to use a different number of processes, e.g. 4, change the command to ```asyc.bat % --processes=4```.

Similar changes might be possible on other editors.
