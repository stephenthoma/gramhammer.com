'use strict';

/*global inject, describe, it, module, beforeEach, expect, ImageCtrl*/

describe('ImageCtrl', function() {
  var $rootScope, $httpBackend, requestHandler, createController;

  beforeEach(function() {
    module('gramhammer');
  });

  beforeEach(inject(function ($injector) {
    $httpBackend = $injector.get('$httpBackend');
    requestHandler = $httpBackend.whenGET('/api/image')
      .respond({
        image: {
          id: 1,
          url: 'http://placehold.it/800x800',
          description: 'This is a placeholder image: edgy.',
          user: 1
        }
      });

    $rootScope = $injector.get('$rootScope');

    var $controller = $injector.get('$controller');
    createController = function () {
          return $controller(ImageCtrl, {'$scope': $rootScope });
        };
  }));

  it('should always be true', function() {
    expect(true).toBe(true);
  });

  it('should attach image to scope', function() {
    $httpBackend.expectGET('/api/image');

    var controller = createController();
    $httpBackend.flush();

    expect($rootScope.image).toBeDefined();
  });
});
