FROM ruby:3.1

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

WORKDIR /usr/src/notifer-frontend

COPY Gemfile Gemfile.lock ./
RUN bundle install
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/notifer-frontend/entrypoint.sh
ADD . ./

ENTRYPOINT [ "/usr/src/notifer-frontend/entrypoint.sh" ]