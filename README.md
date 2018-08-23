# 2018-10
Class for SAVI 810 (Intro to Python Scripting for Geospatial), Fall (October-November) 2018

This semester we'll be staying within the ArcGIS Pro Python environment so we don't spend too much time dealing with cross-platform and environment/dependencies issues. 

We'll be using Python 3.x as well. 

https://answers.microsoft.com/en-us/windows/forum/windows_10-other_settings/how-can-i-download-windows-10-pro-trial-version/caad016a-1069-4a0e-958d-769e26192d62


# 2017-10
Class for SAVI 810 (Intro to Python Scripting for Geospatial), Fall (October-November) 2017 

We'll be using [`virtualenv`](https://pypi.python.org/pypi/virtualenv), "a tool to create isolated Python environments." [https://pypi.python.org/pypi/virtualenv](https://pypi.python.org/pypi/virtualenv)

To get all the Python dependencies for the class 

1. Install [`virtualenv`](https://pypi.python.org/pypi/virtualenv)
2. Then do:

		virtualenv env
		pip install jupyter
		
FYI, you may have to do `sudo xcodebuild -license` for MacOS High Sierra (I just did update), scroll through directions and type `agree` and press [return].

3. Then install pandas, matplotlib.
		
		pip install pandas
		pip install matplotlib
		
		
		
