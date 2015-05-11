#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")


class ForenzikHandler(BaseHandler):
    def post(self):
        dnk = self.request.get("dnk")

        blCrna = "CCAGCAATCGC"
        blRjava = "GCCAGTGCCG"
        blKoren = "TTAGCTATCGC"

        ooKvadrat = "GCCACGG"
        ooOkrogel = "ACCACAA"
        ooOvalen = "AGGCCTCA"

        boModra = "TTGTGGTGGC"
        boZelena = "GGGAGGTGGC"
        boRjava = "AAGTAGTGAC"

        spM = "TGCAGGAACTTC"
        spZ = "TGAAGGACCTTC"

        rBel = "AAAACCTCA"
        rCrn = "CGACTACAG"
        rAzj = "CGCGGGCCG"

        if dnk.find(blCrna) != -1:
            lasje = "Barva las je crna"
        elif dnk.find(blRjava) != -1:
            lasje = "Barva las je rjava"
        elif dnk.find(blKoren) != -1:
            lasje = "Barva las je oranžna"

        if dnk.find(ooKvadrat) != -1:
            obraz = "Oblika obraza je kvadratna"
        elif dnk.find(ooOkrogel) != -1:
            obraz = "Oblika obraza je okrogla"
        elif dnk.find(ooOvalen) != -1:
            obraz = "Oblika obraza je ovalna"

        if dnk.find(boModra) != -1:
            oci = "Barva oci je modra"
        elif dnk.find(boZelena) != -1:
            oci = "Barva oci je zelena"
        elif dnk.find(boRjava) != -1:
            oci = "Barva oci je rjava"

        if dnk.find(spM) != -1:
            spol = "Spol je moski"
        elif dnk.find(spZ) != -1:
            spol = "Spol je zenski"

        if dnk.find(rBel) != -1:
            rasa = "Rasa je belec"
        elif dnk.find(rCrn) != -1:
            rasa = "Rasa je crnec"
        elif dnk.find(rAzj) != -1:
            rasa = "Rasa je azijec"

        params = {"dnk": dnk, "lasje": lasje, "obraz": obraz, "oci": oci, "spol": spol, "rasa": rasa}
        self.render_template("forenzik.html", params)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/forenzik', ForenzikHandler)
], debug=True)
