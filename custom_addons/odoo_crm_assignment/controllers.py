# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ExternalEnquiryController(http.Controller):

    @http.route('/api/external-enquiry', type='http', auth='public', methods=['POST'], csrf=False, website=True)
    def receive_enquiry(self, **post):
        # Extract form inputs
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        campus = post.get('campus')
        course = post.get('course')
        utm_source = post.get('utm_source')
        utm_medium = post.get('utm_medium')
        utm_campaign = post.get('utm_campaign')
        landing_page_url = post.get('landing_page_url')

        # Find target stage "New Enquiry"
        stage = request.env['crm.stage'].sudo().search([('name', '=', 'New Enquiry')], limit=1)

        # Write lead to CRM database table
        lead = request.env['crm.lead'].sudo().create({
            'name': f"Enquiry: {name} ({course})",
            'contact_name': name,
            'email_from': email,
            'phone': phone,
            'description': (
                f"Campus: {campus}\n"
                f"Course: {course}\n"
                f"UTM Source: {utm_source}\n"
                f"UTM Medium: {utm_medium}\n"
                f"UTM Campaign: {utm_campaign}\n"
                f"Landing Page URL: {landing_page_url}"
            ),
            'stage_id': stage.id if stage else False,
            'type': 'opportunity',
        })

        return f"<h2 style='font-family:sans-serif; color:green;'>Enquiry successfully received! Lead ID created in Odoo CRM: {lead.id}</h2>"