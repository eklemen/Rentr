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
    
    var totes = Restangular.all("rentable");
    totes.getList().then(function(rentable){
        $scope.rentable = rentable;
//        console.log(rentable[0]);
//        return self.rentable;
    });
}); //end controller