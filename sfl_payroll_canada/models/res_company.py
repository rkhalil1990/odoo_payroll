# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm


class ResCompany(orm.Model):
    _inherit = 'res.company'
    _columns = {
        'cra_transmitter_number': fields.char(
            'Canada Revenu Agency Transmitter Number',
            help="The first time you send a T4 summary, you must use "
            "the number MM000000. When the CRA receives your first summary, "
            "they will create and send you a number to replace MM000000.",
        ),
        'cra_payroll_number': fields.char(
            'CRA Payroll Number', size=15,
            help="This number contains the buisness number followed by RP and "
            "the payroll account number 4 digits"
        ),
    }

    _defaults = {
        'cra_transmitter_number': 'MM000000',
    }