'use strict';

var app = angular.module('rentr', ['ngResource']);

// changes syntax of angular so its not the same as django
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// factory for all the api calls
app.factory('rentFactory', function($resource){
    return $resource('/rentable.json');

});

app.controller('MainController', function($scope, rentFactory) {
    $scope.world = 'World';
    $scope.names = ['foo', 'bar', 'baz', 'bat'];
    $scope.foo = rentFactory.query();
    console.log($scope.foo);
});