# language: en

Feature: Search games by rating

  @gamesByRating
Scenario: Filtering games with the option rate "T"
    Given the user selects one or more ratings
     | CATEGORY                   |
     | E                          |
     | T                          |
     | M                          |
    When choosing the search by ratings option
    And the games are
      | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
     | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
     | Splatoon                   | 2016         | Nintendo             | T      |
     | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
     | The Last of Us             | 2013         | Naughty Dog          | M      |

    Then 1 game will match
    And the names of these games are
    | NAME                       |
    | Splatoon                   |

    Then following message will be displayed: 1 game was found with rate 'T'


  @gamesByRating
  Scenario: As a user I want to view a list of the games by rating, selecting one or more categories [E, T, M] to find games by type of audience.
     Given the user selects one or more ratings
     | CATEGORY                   |
     | E                          |
     | T                          |
     | M                          |
     When choosing the search by ratings option
     And the games are
     | NAME                       | RELEASE DATE | DEVELOPER            | RATE   |
     | The Witcher 3: Wild Hunt   | 2015         | CD Projekt           | M      |
     | Splatoon                   | 2016         | Nintendo             | T      |
     | Super Smash Bros. Ultimate | 2018         | Bandai Namco Studios | E      |
     | The Last of Us             | 2013         | Naughty Dog          | M      |
     But there is no match with the list of games
     Then following message will be displayed: No game with the specified rating was found.


