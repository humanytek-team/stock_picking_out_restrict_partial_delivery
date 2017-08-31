# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import api, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _

class stock_backorder_confirmation(models.TransientModel):
    _inherit = 'stock.backorder.confirmation'

    @api.multi
    def _process(self, cancel_backorder=False):

        if not self.pick_id.authorize_partial_delivery:
            raise ValidationError(
                _('Partial delivery is not permitted for this transfer. Check with your stock manager')
                )

        return super(stock_backorder_confirmation, self)._process(
            cancel_backorder)
