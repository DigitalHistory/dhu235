#!/bin/sh

# DIR=$(dirname "$0")

DIR=/home/matt/wdw235
HUGODIR=$DIR/website
RENDERED=website/public

# cd $DIR/..

cd $DIR


# if [[ $(git status -s) ]]
# then
#   echo "The working directory is dirty. Please commit any pending changes."
#   exit 1;
# fi

echo "Deleting old rendered site"
rm -rf $RENDERED
mkdir $RENDERED
git worktree prune
rm -rf .git/worktrees/$RENDERED/

echo "Checking out gh-pages branch into $RENDERED"
git worktree add -B gh-pages $RENDERED origin/gh-pages

echo "Removing existing files"
rm -rf public/*

echo "Generating site"
cd $HUGODIR
hugo 

echo "Updating gh-pages branch"
cd $DIR/$RENDERED && git add --all && git commit -m "Publishing to gh-pages (publish.sh)"
git push origin gh-pages
