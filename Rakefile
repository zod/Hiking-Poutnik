require 'rake/clean'
require 'json'

task :default => ['Walking', 'Hiking_SAC2']

task :Walking => ['Walking.brf', 'Walking-wet.brf']
CLOBBER.include(Rake::Task[:Walking].prerequisites)

task :Hiking_SAC2 => ['Hiking_SAC2.brf', 'Hiking_SAC2-SHRP.brf', 'Hiking_SAC2-VSHRP.brf']
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

# FIXME add json files to CLEAN/CLOBBER
# Walking-wet.json -> Walking.json, wet.json
rule( /-.*\.json$/ => [
  proc { |tn| [tn.sub(/-.*.json$/, '.json'), tn.sub(/^.*-/, '')] }
]) do |t|
  puts "Merging #{t.prerequisites.join(', ')} -> #{t.name}"
  # Merge all prerequisites (last file wins)
  merge_json(t.prerequisites, t.name)
end
