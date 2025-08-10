/*
 * Use `npm install` to install all the dependencies located in package.json
 * Then `gulp default` to minimize css and images.
 */
const gulp = require('gulp');
const concat = require('gulp-concat');
const uglify = require('gulp-terser');

gulp.task('js', gulp.parallel(function() {
    return gulp.src(['js/_partials/main/**.js'])
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .on('error', (err) => {
            console.log(err.toString());
        })
        .pipe(gulp.dest("js/"))
    }, function() {
        return gulp.src(['js/_partials/disqus/**.js'])
            .pipe(concat('disqus.min.js'))
            .pipe(uglify())
            .on('error', (err) => {
                console.log(err.toString());
            })
            .pipe(gulp.dest("js/"))
    }, function() {
        return gulp.src(['js/_partials/juxtapose/**.js'])
        .pipe(concat('juxtapose.min.js'))
        .pipe(uglify())
        .on('error', (err) => {
            console.log(err.toString());
        })
        .pipe(gulp.dest("js/"))
    })
);

gulp.task("default", gulp.series("js"));
