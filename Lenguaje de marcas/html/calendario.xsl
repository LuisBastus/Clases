<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="text" encoding="UTF-8"/>

  <xsl:template match="/calendari">
    <xsl:text>BEGIN:VCALENDAR&#xA;</xsl:text>
    <xsl:text>VERSION:2.0&#xA;</xsl:text>
    <xsl:text>PRODID:-//El Ruc//Generador ICS//CA&#xA;</xsl:text>
    <xsl:apply-templates select="esdeveniment"/>
    <xsl:text>END:VCALENDAR</xsl:text>
  </xsl:template>

  <xsl:template match="esdeveniment">
    <xsl:variable name="posicio" select="position()"/>
    <xsl:text>BEGIN:VEVENT&#xA;</xsl:text>
    <xsl:text>UID:</xsl:text>
    <xsl:value-of select="$posicio"/>
    <xsl:text>&#xA;</xsl:text>
    <xsl:text>DTSTAMP:20250410T090000&#xA;</xsl:text>
    <xsl:text>SUMMARY:</xsl:text>
    <xsl:value-of select="titol"/>
    <xsl:text>&#xA;</xsl:text>
    <xsl:text>DTSTART:</xsl:text>
    <xsl:value-of select="dataInici"/>
    <xsl:text>&#xA;</xsl:text>
    <xsl:text>DTEND:</xsl:text>
    <xsl:value-of select="dataFi"/>
    <xsl:text>&#xA;</xsl:text>
    <xsl:text>END:VEVENT&#xA;</xsl:text>
  </xsl:template>
</xsl:stylesheet>