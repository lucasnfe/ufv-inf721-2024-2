---
layout: home
title: INF721 - Deep Learning
nav_exclude: true
permalink: /:path/
seo:
  type: Course
  name: INF721 - Deep Learning
---

## INF721 - Deep Learning (2024/2)

This course introduces students to the fundamentals and modern techniques of Deep Learning, aiming at enabling students to design and implement deep neural networks for classification, regression, and generation of unstructured data.

## Announcements

{% assign announcements = site.announcements %}
{{ announcements.last }}

## Lectures

- Mondays 2:00-3:40pm, CCE406
- Wednesdays 4:00-5:40pm, CCE406

## Instructor

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}
