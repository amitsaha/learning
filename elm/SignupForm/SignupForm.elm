-- declares that this is the SignupForm module, which is how
-- other modules will reference this one if they want to import it and reuse its code.
module SignupForm where

import StartApp
import Effects
import Html exposing (..)
import Html.Events exposing (..)
import Html.Attributes exposing (id, type', for, value, class)

view actionDispatcher model =
    form
        [ id "signup-form" ]
        [ h1 [] [ text "Sensational Signup Form" ]
        , label [ for "username-field" ] [ text "username: " ]
        , input [ id "username-field"
                , type' "text"
                , value model.username
                , on "input" targetValue (\str -> Signal.message actionDispatcher {actionType = "SET_USERNAME", payload = str})
                ] []
        , div [class "validation-error" ] [ text model.errors.username ]
        , label [ for "password" ] [ text "password: " ]
        , input [ id "password-field"
                , type' "text"
                , value model.password
                , on "input" targetValue (\str -> Signal.message actionDispatcher {actionType = "SET_PASSWORD", payload = str})
                ] []
        , div [class "validation-error" ] [ text model.errors.password ]
        , div [ class "signup-button", onClick actionDispatcher { actionType = "VALIDATE", payload = "" } ] [ text "Sign Up!" ] 
        ]


getErrors model =
  { username =
      if model.username == "" then
        "Please enter a username"
      else
        ""
  , password =
      if model.password == "" then
        "Please enter a password"
      else
        ""
  }

update action model =
  if action.actionType == "VALIDATE" then
    ( { model | errors = getErrors model }, Effects.none )
  else if action.actionType == "SET_USERNAME" then
    ( { model | username = action.payload }, Effects.none)
  else if action.actionType == "SET_PASSWORD" then
    ( { model | password = action.payload }, Effects.none)
  else
    (model, Effects.none)

initialModel = { username = "", password = "", errors = initialErrors }
initialErrors = { username = "", password = ""}
app =
  StartApp.start
            { init = ( initialModel, Effects.none )
            , update = update
            , view = view
            , inputs = []
            }
main =
  app.html
