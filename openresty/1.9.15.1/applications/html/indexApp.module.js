'use strict';

// Define the `demoApp` module
var indexAppModule = angular.module('indexApp', [
    // ...which depends on the `phoneList` module
    'ngRoute',
    'ngResource',
    'ngAnimate',
    
    'authTest',
    
    /* 'core',
    'commonList',
    'phoneList',
    'phoneDetail' */
]);
