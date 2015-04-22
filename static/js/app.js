'use strict';

var app = angular.module('rentr', ['restangular']);

// changes syntax of angular so its not the same as django
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// factories for api calls
app.factory('Rent', function(Restangular){
    return Restangular.all("rentable");
});

// main controller
app.controller('MainController', function($scope, Restangular, Rent) {
    $scope.world = 'World';
    $scope.names = ['foo', 'bar', 'baz', 'bat'];

    var totes = Restangular.all("rentable");
    Rent.getList().then(function(rentable){
        $scope.rentable = rentable;
        console.log(rentable[0]);
        console.log(rentable[1]);
//        return self.rentable;
    });
}); //end controller