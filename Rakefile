require 'rake/clean'
require 'json'

task :default => ['Walking', 'Hiking_SAC2']

task :Walking => ['Walking.brf', 'Walking-wet.brf']
CLOBBER.include(Rake::Task[:Walking].prerequisites)

task :Hiking_SAC2 => ['Hiking-SAC2.brf', 'Hiking-SAC2-SHRP.brf']
CLOBBER.include(Rake::Task[:Hiking_SAC2].prerequisites)

rule '.brf' => ['.json'] do |t| 
  sh "mustache #{t.source} Hiking.mustache > #{t.name}"
end

def merge_json(files_input, file_output)
  config = files_input.map do |filename|
    JSON.parse(File.read(filename))
  end.reduce({}) do |memo, obj|
    memo.merge(obj)
  end
  File.open(file_output, 'w') do |f|
    JSON.dump(config, f)
  end
end

# FIXME merge three rules into one
# FIXME add json files to CLEAN/CLOBBER
rule '-wet.json' => [
  proc { |tn| [tn.sub('-wet.json', '.json'), 'wet.json'] }
] do |t|
  # Merge all prerequisites (last file wins)
  merge_json(t.prerequisites, t.name)
end

rule '-SHRP.json' => [
  proc { |tn| [tn.sub('-SHRP.json', '.json'), 'SHRP.json'] }
] do |t|
  # Merge all prerequisites (last file wins)
  merge_json(t.prerequisites, t.name)
end

rule '-VSHRP.json' => [
  proc { |tn| [tn.sub('-VSHRP.json', '.json'), 'VSHRP.json'] }
] do |t|
  # Merge all prerequisites (last file wins)
  merge_json(t.prerequisites, t.name)
end
