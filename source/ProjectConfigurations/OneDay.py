#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @email : spirit_az@foxmail.com
__author__ = 'ChenLiang.Miao'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# 考虑到python2和3的过渡兼容问题，这里不要使用独有库。
import os
import inspect

# import get_all_software

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


def get_file_path(module, basename=True):
    if not basename:
        return module
    return os.path.splitext(os.path.basename(module))[0]


def get_module_path(module):
    """
    return dir for imported module..
    """
    moduleFile = inspect.getfile(module)
    modulePath = os.path.dirname(moduleFile)
    return modulePath


def get_script_path():
    """
    return dir path for used script..
    """
    scriptPath = get_module_path(
        inspect.currentframe().f_back).replace(
        '\\', '/')
    return scriptPath


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
FILENAME = get_file_path(__file__)
basePath = get_script_path().replace('\\', '/')

ProjectName = FILENAME
PIPELINE_SOFTWARE = ''
FPS = 24
UNIT = 'cm'


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# software version
CLARISSE_VERSION = '4.0 SP3'
HIERO_VERSION = '10.5'
hiero_v = 'v2'
HOUDINI_VERSION = "17.0.352"
MAYA_VERSION = "2018"
NUKE_VERSION = '10.5'
PHOTOSHOP_VERSION = 'CC 2015'
RV_VERSION = '7.2.0'
SUBSTANCE_VERSION = ''
SYNTHEYES_VERSION = ''
UE_VERSION = '4.16'
ZBRUSH_VERSION = '4R8'
BLENDER_VERSION = '4R8'

# # exe file
# MAYA_EXE_FILE = get_all_software.search_exe_path(
#     "Autodesk Maya %s" %
#     MAYA_VERSION)
# HOUDINI_EXE_FILE = get_all_software.search_exe_path(
#     "Houdini %s" %
#     HOUDINI_VERSION)

# clarisse
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

CLARISSE_BAT_PATH = {}

CLARISSE_CONF_PATH = os.path.join(
    os.path.dirname(basePath),
    'Clarisse',
    CLARISSE_VERSION).replace(
        '\\',
    '/')

CLARISSE_LOCATION = """
C:/Python27/python.exe "{0}/modify_config.py"  -project_name "{1}"
"C:/Progra~1/Isotropix/Clarisse iFX {2}/Clarisse/clarisse.exe" -startup_script "{0}/startup_script.py" -project_name "{1}" """.format(
    CLARISSE_CONF_PATH, FILENAME, CLARISSE_VERSION)

# hiero
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
HIERO_BAT_PATH = {}

HIERO_LOCATION = """
"C:/Program Files/Nuke{0}{1}/Nuke{0}.exe" --hiero
""".format(HIERO_VERSION, hiero_v)

# houdini
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
PROJECT_HOUDINI_PATH = os.path.dirname(basePath).replace('\\', '/')

HOUDINI_BAT_PATH = dict(HOUDINI_NVIDIA_OPTIX_DSO_PATH=[
    'C:/Program Files/Side Effects Software/Houdini {0}/NVIDIA_OptiX'.format(HOUDINI_VERSION)],
    HOUDINI_OTLSCAN_PATH=['"', '&', os.path.dirname(basePath) + '/Houdini/HDA_Libs/otls',
                          '{0}/Houdini/otls/17'.format(PROJECT_HOUDINI_PATH)],
    PYTHONPATH=['{0}/Houdini/Python/17/Lib/site-packages'.format(PROJECT_HOUDINI_PATH),
                '{0}/Houdini/Scripts/17'.format(PROJECT_HOUDINI_PATH),
                '{0}/Houdini/Tools/17'.format(PROJECT_HOUDINI_PATH),
                '{0}/Houdini/python_Lib2.7'.format(PROJECT_HOUDINI_PATH)

                ],
)

HOUDINI_SESSION_PATH = dict(
    cache_driver='S:',
    render_driver='R:'

)

HOUDINI_LOCATION = '''
"D:/Program Files/Side Effects Software/Houdini {0}/bin/houdinifx.exe" -foreground "{1}/houdiniConf/VHQShelf/17/VHQShelf1.0/scripts/startHoudini.py" "{1}/{2}.py"
'''.format(HOUDINI_VERSION, basePath, FILENAME)

# maya
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
MAYA_PLUGIN_LIST = [
    'projectConfiguration',
    "redshift4maya",
    "dgProfiler",
    "invertShape",
    "mayaHIK",
    "curveWarp",
    "MASH",
    "poseInterpolator",
    "cgfxShader",
    "ikSpringSolver",
    "ik2Bsolver",
    "xgenToolkit",
    "retargeterNodes",
    "OpenEXRLoader",
    "animImportExport",
    "Type",
    "meshReorder",
    "modelingToolkit",
    "deformerEvaluator",
    "matrixNodes",
    "xgSplineDataToXpd",
    "atomImportExport",
    "AbcImport",
    "AbcExport",
    "sceneAssembly",
    "gpuCache",
    "nearestPointOnMesh",
    "objExport",
    "freeze",
    "GPUBuiltInDeformer",
    "stereoCamera",
    "fltTranslator",
    "quatNodes",
    "fbxmaya",
    "glslShader",
    "SHAPESBrush",
    "ngSkinTools",
    "mtoa",
]
PROJECT_MAYA_PATH = os.path.dirname(basePath).replace('\\', '/')


REDSHIFT_CONF = {
    "REDSHIFT_COREDATAPATH": "{0}/Maya/modules/Redshift".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_PLUG_IN_PATH": "{0}/Maya/modules/Redshift/Plugins/Maya/{1}/nt-x86-64".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_SCRIPT_PATH": "{0}/Maya/modules/Redshift/Plugins/Maya/Common/scripts".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_XBMLANGPATH": "{0}/Maya/modules/Redshift/Plugins/Maya/Common/icons".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_RENDER_DESC_PATH": "{0}/Maya/modules/Redshift/Plugins/Maya/Common/rendererDesc".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_CUSTOM_TEMPLATE_PATH": "{0}/Maya/modules/Redshift/Plugins/Maya/Common/scripts/NETemplates".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_MAYAEXTENSIONSPATH": "{0}/Maya/modules/Redshift/Plugins/Maya/{1}/nt-x86-64/extensions".format(
        PROJECT_MAYA_PATH, MAYA_VERSION),
    "REDSHIFT_PROCEDURALSPATH": "{0}/Maya/modules/Redshift/Procedurals".format(
        PROJECT_MAYA_PATH, MAYA_VERSION)


}

MAYA_VARIABLES = {
    'MAYA_SCRIPT_PATH': ['{0}/Maya/Tools/{1}'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/ANI'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/CFX'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/CGTmW'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/EFX'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/ENV'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/GNR'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/GNL'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/LAY'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/LGT'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/MOD'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/REDS'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/RIG'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/SUR'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/TRC'.format(PROJECT_MAYA_PATH, MAYA_VERSION),
                         '{0}/Maya/Tools/{1}/VFX'.format(PROJECT_MAYA_PATH, MAYA_VERSION),

                         ],
    'MAYA_PLUG_IN_PATH': [],


}

MAYA_BAT_PATH = dict(XBMLANGPATH=['{0}/Maya/icons/{1}'.format(PROJECT_MAYA_PATH,
                                                              MAYA_VERSION),
                                  REDSHIFT_CONF['REDSHIFT_XBMLANGPATH']],
                     MAYA_DISABLE_CER=1,
                     MAYA_DISABLE_CLIC_IPM=1,
                     MAYA_UI_LANGUAGE='en_US',
                     MAYA_MODULE_PATH=["{0}/mayaConf/VHQShelf/{1}/VHQShelf1.0".format(basePath,
                                                                                      MAYA_VERSION),
                                       "{0}/Maya/modules/Yeti/{1}/Yeti3.6.2".format(PROJECT_MAYA_PATH,
                                                                                    MAYA_VERSION),
                                       "{}/Maya/modules/ngskintools/Contents".format(
                                           PROJECT_MAYA_PATH),
                                       "{}/Maya/modules/SHAPESBrush/{}/SHAPESBrush1.0".format(PROJECT_MAYA_PATH,
                                                                                              MAYA_VERSION),
                                       "{}/Maya/modules/soup/soup".format(
                                           PROJECT_MAYA_PATH),
                                       "{0}/Maya/modules/mtoa/{1}/mtoa".format(PROJECT_MAYA_PATH,
                                                                               MAYA_VERSION),
                                       ],
                     PYTHONPATH=[os.path.dirname(__file__).replace('\\',
                                                                   '/'),
                                 '{0}/Maya/Python/{1}/Lib/site-packages'.format(PROJECT_MAYA_PATH,
                                                                                MAYA_VERSION),
                                 '{0}/Maya/Tools/{1}'.format(PROJECT_MAYA_PATH,
                                                             MAYA_VERSION),
                                 '{0}/Maya/Scripts/{1}'.format(PROJECT_MAYA_PATH,
                                                               MAYA_VERSION),
                                 REDSHIFT_CONF['REDSHIFT_SCRIPT_PATH']],
                     # MAYA_SHELF_PATH=["{0}/Maya/modules/UVLayout/{1}/UVLayout/shelves".format(PROJECT_MAYA_PATH,
                     #                                                                          MAYA_VERSION),
                     # "{0}/Maya/modules/SOuP/{1}/soup/shelves".format(PROJECT_MAYA_PATH,
                     #                                                 MAYA_VERSION)],
                     REDSHIFT_COREDATAPATH=REDSHIFT_CONF["REDSHIFT_COREDATAPATH"],
                     REDSHIFT_PLUG_IN_PATH=REDSHIFT_CONF["REDSHIFT_PLUG_IN_PATH"],
                     REDSHIFT_SCRIPT_PATH=REDSHIFT_CONF["REDSHIFT_SCRIPT_PATH"],
                     REDSHIFT_XBMLANGPATH=REDSHIFT_CONF["REDSHIFT_XBMLANGPATH"],
                     REDSHIFT_RENDER_DESC_PATH=REDSHIFT_CONF["REDSHIFT_RENDER_DESC_PATH"],
                     REDSHIFT_CUSTOM_TEMPLATE_PATH=REDSHIFT_CONF["REDSHIFT_CUSTOM_TEMPLATE_PATH"],
                     REDSHIFT_MAYAEXTENSIONSPATH=REDSHIFT_CONF["REDSHIFT_MAYAEXTENSIONSPATH"],
                     REDSHIFT_PROCEDURALSPATH="{0}/Maya/modules/Redshift/Procedurals".format(PROJECT_MAYA_PATH,
                                                                                             MAYA_VERSION),
                     REDSHIFT_LICENSEPATH="{0}/Maya/modules/Redshift/lic".format(PROJECT_MAYA_PATH,
                                                                                 MAYA_VERSION),
                     MAYA_PLUG_IN_PATH=[REDSHIFT_CONF["REDSHIFT_PLUG_IN_PATH"]],
                     MAYA_SCRIPT_PATH=[REDSHIFT_CONF["REDSHIFT_SCRIPT_PATH"]],
                     MAYA_RENDER_DESC_PATH=[REDSHIFT_CONF["REDSHIFT_RENDER_DESC_PATH"]],
                     MAYA_CUSTOM_TEMPLATE_PATH=[REDSHIFT_CONF["REDSHIFT_CUSTOM_TEMPLATE_PATH"]],
                     PATH=[REDSHIFT_CONF["REDSHIFT_COREDATAPATH"] + "/bin"],
                     PEREGRINEL_LICENSE="{0}/Maya/modules/Yeti/{1}/Yeti3.6.2/lic/yeti.lic".format(PROJECT_MAYA_PATH,
                                                                                                  MAYA_VERSION),
                     )

MAYA_LOCATION = """
"D:/Program Files/Autodesk/Maya{0}/bin/maya.exe" -noAutoloadPlugins -command "loadPlugin \\"projectConfiguration.py\\";projectConf -ls all -lp \\"{1}\\";"
""".format(MAYA_VERSION, __file__.replace('\\', '/'))  #

# nuke
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
PROJECT_NUKE_PATH = os.path.join(os.path.dirname(basePath), "Nuke")
NUKE_BAT_PATH = {
    # http://help.thefoundry.co.uk/nuke/8.0/content/user_guide/configuring_nuke/nuke_environment_variables.html
    'NUKE_PATH': ["{0}/{1}".format(PROJECT_NUKE_PATH, NUKE_VERSION)]
    # 'OFX_PLUGIN_PATH': [PROJECT_NUKE_PATH],
    # 'PYTHONPATH': [PROJECT_NUKE_PATH]

}

NUKE_LOCATION = '"C:/Program Files/Nuke{0}v2/Nuke{0}.exe" --nukex "{1}" "{2}"'.format(
    NUKE_VERSION, '', FILENAME)

# photoshop
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
PHOTOSHOP_BAT_PATH = {}

PHOTOSHOP_LOCATION = """
"C:/Program Files/Adobe/Adobe Photoshop {}/Photoshop.exe"
""".format(PHOTOSHOP_VERSION)

# shotgun rv
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
RV_BAT_PATH = {}

RV_LOCATION = """
"C:/Program Files/Shotgun/RV-{}/bin/rv.exe"
""".format(RV_VERSION)

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
SUBSTANCE_BAT_PATH = {}

SUBSTANCE_LOCATION = """
"D:/Program Files/Allegorithmic/Substance Painter/Substance Painter.exe"
"""

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
SYNTHEYES_BAT_PATH = {}

SYNTHEYES_LOCATION = """
"C:/Program Files/Andersson Technologies LLC/SynthEyes/SynthEyes64.exe"
"""

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
UE_BAT_PATH = {}

UE_LOCATION = """
"D:/Epic Games/UE_{0}/Engine/Binaries/Win64/UE4Editor.exe"
""".format(UE_VERSION)

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
ZBRUSH_BAT_PATH = {}

ZBRUSH_LOCATION = """
"D:/program Files/Pixologic/ZBrush {}/ZBrush.exe"
""".format(ZBRUSH_VERSION)

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
BLENDER_BAT_PATH = {}

BLENDER_LOCATION = """
"D:/Program Files/Blender Foundation/Blender/blender.exe"
""".format(BLENDER_VERSION)


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
