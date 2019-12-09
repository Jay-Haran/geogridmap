from distutils.core import setup

setup(name='geogridmap',
            version = '0.1',
            description= 'Plotting a probability distribution over a geographic over maps',
            packages = ['geogridmap'],
            author = 'Jay Haran',
      install_requires = [itertools,json, branca.element, folium, folium.plugins, numpy, pandas, scipy.optimize,
                          scipy.stats])