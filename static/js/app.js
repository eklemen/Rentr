'use strict';

var app = angular.module('rentr', ['ngResource', 'restangular']);

// changes syntax of angular so its not the same as django
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// factory for api calls
//app.factory('rentFactory', function($resource){

//});

// main controller
app.controller('MainController', function($scope, Restangular) {
    $scope.world = 'World';
    $scope.names = ['foo', 'bar', 'baz', 'bat'];
    
    var total = Restangular.all('rentable', '/rentable').getList();

    console.log(total);
    
    var rentable = [];
    var totes = Restangular.all("rentable/");
    $scope.rentable = totes.getList().then(function(rentable){
        console.log(rentable[0]);
        return rentable;
    })
    console.log($scope.rentable);
});