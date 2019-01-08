#!/usr/bin/env python
import os
import glob
import jinja2
import click


@click.command()
@click.option('-t', '--tag', default='')
def make_templates(tag):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('default')
    if tag:
        folder = tag
        os.mkdir(folder)
    else:
        folder = '.'
    for cuda in (False, True):
        for system in ('flux', 'comet', 'bridges'):
            tag_ = str(tag)
            if tag_ and not tag_.endswith('-'):
                tag_ += '-'
            tag_ += 'cuda8-' + system if cuda else system
            image = 'glotzerlab/software:' + tag_
            fn = os.path.join(folder, 'Singularity.' + tag_)
            print("Building '{}'...".format(image))
            recipe = template.render({'base_image': image})
            with open(fn, 'w') as recipe_file:
                recipe_file.write(recipe + '\n')


if __name__ == '__main__':
    make_templates()
