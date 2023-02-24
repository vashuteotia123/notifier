#!/bin/sh
bundle exec rails db:migrate -e production
bundle exec rails s -e production -b '0.0.0.0'
