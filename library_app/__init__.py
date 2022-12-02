from . import models
from . import controllers

from odoo import api, fields, SUPERUSER_ID, _


def _uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
     
    env.ref('library_app.library_group_manager', raise_if_not_found=False).sudo().write({'name': 'Librarian'})
