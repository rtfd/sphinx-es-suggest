"use strict";

var autoprefixer = require("gulp-autoprefixer"),
    csso = require("gulp-csso"),
    del = require("del"),
    gulp = require("gulp"),
    rename = require("gulp-rename"),
    runSequence = require("run-sequence"),
    uglify = require("gulp-uglify"),
    babel = require("gulp-babel");

gulp.task("styles", function() {
    return gulp
        .src("sphinx_search/_static/css/*.css")
        .pipe(autoprefixer())
        .pipe(csso())
        .pipe(rename({ extname: ".min.css" }))
        .pipe(gulp.dest("sphinx_search/_static/css"));
});

gulp.task("scripts", function() {
    return gulp
        .src("sphinx_search/_static/js/*.js")
        .pipe(babel({ presets: ["@babel/env"] }))
        .pipe(uglify())
        .pipe(rename({ extname: ".min.js" }))
        .pipe(gulp.dest("sphinx_search/_static/js"));
});

gulp.task("clean", function() {
    return del(["sphinx_search/**/*.min.*"]);
});

gulp.task("default", ["clean"], function() {
    runSequence("styles", "scripts");
});
