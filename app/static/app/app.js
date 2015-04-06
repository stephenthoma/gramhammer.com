'use strict';

angular.module('gramhammer', [
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider, $locationProvider, $httpProvider) {
    $routeProvider
      .when('/', {
        title: 'Welcome',
        templateUrl: 'static/app/views/home.html',
      })
      .when('/login', {
        title: 'Log In',
        templateUrl: 'static/app/views/login.html'
      })
      .when('/register', {
        title: 'Register',
        templateUrl: 'static/app/views/register.html'
      })
      .otherwise({
        redirectTo: '/'
      });

    $locationProvider.html5Mode(true);

    $httpProvider.interceptors.push(['$q', '$location', function($q, $location) {
      return {
        'responseError': function(response) {
          if(response.status === 401 || response.status === 403) {
            $location.path('/login');
            return $q.reject(response);
          }
          else {
            return $q.reject(response);
          }
        }
      };
    }]);
  })
  .run(function ($rootScope) {

    $rootScope.$on('$routeChangeSuccess', function (event, current) {
      $rootScope.title = current.$$route.title;
    });

  });
