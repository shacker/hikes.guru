# hikes.guru

To get SASS compiler `sassc`:

```
brew install libsass
brew install sassc
```

Compiling SASS

Libsass bundles the command line tool `sassc`. Customizations go in `static/styles/sass/app.scss` and in the `partials` folder inside. To compile:

`sassc guru/static/styles/sass/app.scss guru/static/styles/css/app.css`

Add -w in another terminal to "watch" the directory (real-time recompilation).
