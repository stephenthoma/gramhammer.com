'use strict';

angular.module('gramhammer')
.factory('ImageService',
    ['$http',
    function ($http) {
      var service = {};

      service.getImage = function () {
        return $http.get('/api/image');
      };

      service.likeImage = function (imageId) {
        return $http.post('/api/image/' + imageId + '/like');
      };

      return service;
    }]);
