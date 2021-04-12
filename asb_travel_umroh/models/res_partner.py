from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    hotel = fields.Boolean(string='Is a Hotel',
                           help="Check this box if this contact is a Hotel. It can be selected in Travel Hotel.")
    airlines = fields.Boolean(string='Is a Airlines',
                              help="Check this box if this contact is a airlines. It can be selected in Airlines.")
