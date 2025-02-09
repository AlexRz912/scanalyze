import os
import time

from modules.assetReconModule import assetReconModule
from helpers.reconHelpers import pendingReconHelper
from helpers.reconHelpers import reconStateHelpers
from helpers.domainFileHelpers import compareToPreviousHelper
from helpers.domainFileHelpers import buildDomainPathHelper
from helpers import configHelper
from utils.fileUtils import lineNumUtil
from utils.ioUtils import inputUtils

def domain_file_has_changed(path):
    previous_domain_file = buildDomainPathHelper.build_path(path, False)
    new_domain_file = buildDomainPathHelper.build_path(path, True)

    new_file_line_num = lineNumUtil.get_line_num(new_domain_file)
    previous_file_line_num = lineNumUtil.get_line_num(previous_domain_file)

    return compareToPreviousHelper.compare(new_file_line_num, previous_file_line_num)

def domains_file_empty(path):
    domain_file = buildDomainPathHelper.build_path(path, True)
    return lineNumUtil.get_line_num(domain_file) < 1

def is_new_project(config):
    return config["new_project"]

