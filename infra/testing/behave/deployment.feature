Feature: Check we have git
  Scenario: test we have git installed
     Given we are on Linux
     then git should be installed    