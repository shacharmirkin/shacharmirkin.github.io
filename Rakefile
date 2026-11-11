# frozen_string_literal: true

require "fileutils"

task default: :test

desc "Build Jekyll site into _site"
task :build do
  sh "bundle exec jekyll build --destination _site"
  agent_index = File.expand_path("agent-index.source.md", __dir__)
  # Not index.md: GitHub Pages 404s it when index.html exists.
  FileUtils.cp(agent_index, File.expand_path("agent-index.md", "_site"))
end

desc "Run HTMLProofer on _site (run :build first)"
task proof: :build do
  require "html_proofer"
  HTMLProofer.check_directory(
    "./_site",
    {
      disable_external: true,
      assume_extension: true,
      allow_hash_href: true,
    },
  )
end

desc "Build and verify the site"
task test: :proof
