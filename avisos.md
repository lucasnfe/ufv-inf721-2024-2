---
layout: page
title: Announcements
nav_exclude: false
description: A feed containing all of the class announcements.
---

# Announcements

All announcements since the beggining of the course:

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
