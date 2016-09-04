{-# LANGUAGE OverloadedStrings #-}
module Lib
    ( someFunc
    ) where

import Control.Monad.State
import Network.MessagePack.Client


someFunc :: IO ()
someFunc = execClient "localhost" 3000 $ do
    ret <- foo 123 456
    liftIO $ print ret

foo :: Int -> Int -> Client Int
foo = call "func"


