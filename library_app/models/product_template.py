from odoo import fields, models
from odoo.exceptions import ValidationError



class Book(models.Model):
    _inherit = 'product.template'
    _description = 'Book'

    is_book = fields.Boolean(string="Is Book")
    date_published = fields.Date()
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")

    def _check_barcode(self):
        self.ensure_one()
        digits = [int(x) for x in self.barcode if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_barcode(self):
        for book in self:
            if not book.barcode:
                raise ValidationError("Please provide an Barcode for %s" % book.name)
            if book.barcode and not book._check_barcode():
                raise ValidationError("%s Barcode is invalid" % book.barcode)
        return True
