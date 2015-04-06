var gulp = require('gulp');

var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var karma = require('karma').server;

var paths = {
  scripts: 'app/static/js/**/*',
  styles: 'app/static/scss/**/*',
  bootstrap: 'app/static/bower_components/sass-bootstrap/lib/*',
  font_awesome: 'app/static/bower_components/font-awesome/css/font-awesome.css',
  images: 'app/static/img/**/*'
};

gulp.task('test', function () {
  karma.start({
    configFile: __dirname + '/karma.conf.js',
    singleRun: true
  });
});

gulp.task('tdd', function (done) {
  karma.start({
    configFile: __dirname + '/karma.conf.js'
  });
});

gulp.task('styles', function () {
  gulp.src(paths.styles)
    .pipe(sass())
    .pipe(concat('styles.css'))
    .pipe(gulp.dest('app/static/dist/css'));
});

gulp.task('vendor-styles', function() {
  gulp.src([paths.bootstrap, paths.font_awesome])
    .pipe(sass())
    .pipe(concat('vendor.css'))
    .pipe(gulp.dest('app/static/dist/css'));
});

gulp.task('scripts', function() {
  // Minify and copy all JavaScript
  return gulp.src(paths.scripts)
    .pipe(uglify())
    .pipe(concat('main.min.js'))
    .pipe(gulp.dest('app/static/dist/js'));
});

gulp.task('images', function() {
 return gulp.src(paths.images)
    // Pass in options to the task
    .pipe(imagemin({optimizationLevel: 5}))
    .pipe(gulp.dest('app/static/dist/img'));
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(paths.styles, ['styles']);
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch(paths.images, ['images']);
});

gulp.task('default', ['styles', 'vendor-styles', 'scripts', 'images', 'watch']);
