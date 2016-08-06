# hikes.guru

## Local settings

You'll need:

```

SOCIAL_AUTH_TWITTER_KEY = 'something'
SOCIAL_AUTH_TWITTER_SECRET = 'something'

ADMINS = [
    ('Your Name', 'you@example.com'),
]

# Print emails to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

```

## SASS

To get SASS compiler `sassc`:

```
brew install libsass
brew install sassc
```

Customizations go in `static/styles/sass/app.scss` and in the `partials` folder within. To compile:

`sassc project/static/styles/sass/app.scss project/static/styles/css/app.css`

Add -w in another terminal to "watch" the directory (real-time recompilation).


Generate test data with randomized titles, regions, descriptions and directions:
Enable `autofixture` in `INSTALLED_APPS`, then:
`./manage.py loadtestdata trails.Trail:1000`
`./manage.py random_titles`
