import os
import glob
import jinja2


if __name__ == '__main__':
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('default')
    for cuda in (False, True):
        for system in ('flux', 'comet', 'bridges'):
            tag = 'cuda8-' + system if cuda else system
            image = 'glotzerlab/software:' + tag
            fn = 'Singularity.' + tag
            print("Building '{}'...".format(image))
            recipe = template.render({'base_image': image})
            with open(fn, 'w') as recipe_file:
                recipe_file.write(recipe + '\n')
