# sunglasses v0.1.0
# Copyright © 2019 Boian Berberov
#
# Released under the terms of the
# European Union Public License version 1.2 only.
#
# License text: https://joinup.ec.europa.eu/collection/eupl/eupl-text-11-12
#
# SPDX-License-Identifier: EUPL-1.2

from os import path

#
# URL settings
#

ARTICLE_URL=                  'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS=              ARTICLE_URL
ARTICLE_LANG_URL=             'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.{lang}.html'
ARTICLE_LANG_SAVE_AS=         ARTICLE_LANG_URL
PAGE_URL=                     '{category}/{slug}.html'
PAGE_SAVE_AS=                 PAGE_URL
PAGE_LANG_URL=                '{category}/{slug}.{lang}.html'
PAGE_LANG_SAVE_AS=            PAGE_LANG_URL

DRAFT_URL=                    'drafts/blog/{slug}.html'
DRAFT_SAVE_AS=                DRAFT_URL
DRAFT_LANG_URL=               'drafts/blog/{slug}.{lang}.html'
DRAFT_LANG_SAVE_AS=           DRAFT_LANG_URL
DRAFT_PAGE_URL=               'drafts/{slug}.html'
DRAFT_PAGE_SAVE_AS=           DRAFT_PAGE_URL
DRAFT_PAGE_LANG_URL=          'drafts/{slug}.{lang}.html'
DRAFT_PAGE_LANG_SAVE_AS=      DRAFT_PAGE_LANG_URL

AUTHOR_URL=                   'blog/authors/{slug}.html'
AUTHOR_SAVE_AS=               AUTHOR_URL
CATEGORY_URL=                 'blog/categories/{slug}.html'
CATEGORY_SAVE_AS=             CATEGORY_URL
TAG_URL=                      'blog/tags/{slug}.html'
TAG_SAVE_AS=                  TAG_URL

YEAR_ARCHIVE_URL=             'blog/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS=         path.join( YEAR_ARCHIVE_URL, 'index.html' )
MONTH_ARCHIVE_URL=            'blog/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS=        path.join( MONTH_ARCHIVE_URL, 'index.html' )
DAY_ARCHIVE_URL=              'blog/{date:%Y}/{date:%m}/{date:%d}/'
DAY_ARCHIVE_SAVE_AS=          path.join( DAY_ARCHIVE_URL, 'index.html' )

INDEX_SAVE_AS=                'blog/index.html'
ARCHIVES_SAVE_AS=             'blog/archive.html'
AUTHORS_SAVE_AS=              'blog/authors/index.html'
CATEGORIES_SAVE_AS=           'blog/categories/index.html'
TAGS_SAVE_AS=                 'blog/tags/index.html'
