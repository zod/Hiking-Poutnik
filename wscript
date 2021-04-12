#! /usr/bin/env python
# encoding: utf-8

from string import Template
import json

# https://gitlab.com/ita1024/waf/-/blob/master/demos/subst/wscript
# https://gitlab.com/ita1024/waf/-/blob/master/waflib/TaskGen.py#L846

def configure(conf):
    pass

def build(bld):
    def profile_subst(task, text):
        _, _, configs = task.outputs[0].name[:-4].partition('_')
        params = {}
        for config_filename in configs.split('-'):
            config = json.load(open(config_filename + '.json'))
            # FIXME description should be concat
            # config['description'] = params['description']
            params.update(config)

        template = Template(text)
        return template.substitute(params)

    bld(features='subst', subst_fun=profile_subst, source='Hiking.brf.in', target='Hiking_SAC2-SHRP.brf')
