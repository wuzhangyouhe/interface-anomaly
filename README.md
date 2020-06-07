Fix MacOS matplot graph issue.
##
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
brew uninstall python3
brew install python3 --with-tcl-tk
##

Also change function.
##
plt.savefig('myfilename.png')
##