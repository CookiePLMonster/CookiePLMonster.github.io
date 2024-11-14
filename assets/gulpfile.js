/* 
 * Use `npm install` to install all the dependencies located in package.json 
 * Then `gulp default` to minimize css and images.
 */
const gulp = require('gulp');
const concat = require('gulp-concat');
const uglify = require('gulp-terser');
const cleanCSS = require('gulp-clean-css');

gulp.task('js', gulp.parallel(function() {
    return gulp.src(['js/partials/main/**.js'])
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .on('error', (err) => {
            console.log(err.toString());
        })
        .pipe(gulp.dest("js/"))
    }, function() {
        return gulp.src(['js/partials/disqus/**.js'])
            .pipe(concat('disqus.min.js'))
            .pipe(uglify())
            .on('error', (err) => {
                console.log(err.toString());
            })
            .pipe(gulp.dest("js/"))
    }, function() {
        return gulp.src(['js/vendor/juxtapose.min.js'])
        .pipe(concat('juxtapose.min.js'))
        .pipe(uglify())
        .on('error', (err) => {
            console.log(err.toString());
        })
        .pipe(gulp.dest("js/"))
    })
);

gulp.task('css', gulp.parallel(function() {
    return gulp.src('css/vendor/juxtapose.css')
      .pipe(cleanCSS())
      .on('error', (err) => {
        console.log(err.toString())
      })
      .pipe(concat('juxtapose.min.css'))
      .pipe(gulp.dest('css/vendor/'));
  }));

gulp.task("default", gulp.series(gulp.parallel('js', 'css')));
