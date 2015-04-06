'use strict';

function ImageCtrl($scope, $rootScope, $location, ImageService) {
    $scope.init = function () {
      ImageService.getImage()
        .success(function (data) {
          console.log(data);
          $scope.image = {
                          id: data.id,
                          url: data.url,
                          description: data.description,
                          user: data.user,
                          avatar: data.avatar
                         };
        });
    };

    $scope.nextImage = function () {
      ImageService.getImage()
        .success(function (data) {
          console.log(data);
          $scope.image = {
                          id: data.id,
                          url: data.url,
                          description: data.description,
                          user: data.user,
                          avatar: data.avatar
                         };
        });
    };

    $scope.likeImage = function () {
      ImageService.likeImage($scope.image.id)
        .success(function () {
          $scope.nextImage();
        });
    };

    $scope.init();
}


