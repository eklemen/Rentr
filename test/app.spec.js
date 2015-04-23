'use strict';

//describe("hello", function(){
//    it("should work", function(){
//        expect(true).toBe(false);
//    })
//})

describe("testing the MainController", function(){
    beforeEach(module("rentr"));
    var mainCtrl, scope;
    
    beforeEach(inject(function($controller, $rootScope){
        scope = $rootScope;
        mainCtrl = $controller("MainController", {
           $scope: scope 
        });
    }))
    
    
})