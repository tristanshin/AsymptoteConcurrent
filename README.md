# Asymptote Concurrent

A simple script to compile [Asymptote](https://asymptote.sourceforge.io/) concurrently, using Python's multiprocessing package. By default, the script uses half of your available threads but can be told to use a different number via an argument.

**WARNING**: If you overload the script, it may hang unexpectedly. Some ways of doing this include running the script multiple times at the same time or in a row, compiling too many Asymptote files (usually around 100), or having many files require 3D graphics rendering (some issues arise when multiple threads attempt to use Asymptote's 3D graphics renderer at the same time). I am still looking into ways to mitigate these issues.

## Install

The main thing you need is the asyc.py file and a way to run it with command line tools.
- Windows: Clone this repository to your computer and put the folder in your PATH.
- MacOS: Clone this repository to your computer and add the following to your custom bash commands:
```bash
function asyc() {

}
```
