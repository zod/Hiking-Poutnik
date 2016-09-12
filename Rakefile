require 'rake/clean'
require 'json'

task :main => ['Walking.brf', 'Walking-wet.brf', 'Hiking_SAC2.brf', 'Hiking_SAC3.brf']
task :default => ['Walking', 'Hiking_SAC2'] # 'Hiking_SAC3', 'Hiking_SAC4', 'Hiking_SAC5', 'Hiking_SAC6']

task :Walking => ['Walking.brf', 'Walking-wet.brf', 'Walking-SHRP.brf', 'Walking-VSHRP.brf']
task :Hiking_SAC2 => ['Hiking_SAC2.brf', 'Hiking_SAC2-SHRP.brf', 'Hiking_SAC2-VSHRP.brf']
task :Hiking_SAC3 => ['Hiking_SAC3.brf', 'Hiking_SAC3-SHRP.brf', 'Hiking_SAC3-VSHRP.brf']
task :Hiking_SAC4 => ['Hiking_SAC4.brf', 'Hiking_SAC4-SHRP.brf', 'Hiking_SAC4-VSHRP.brf']
task :Hiking_SAC5 => ['Hiking_SAC5.brf', 'Hiking_SAC5-SHRP.brf', 'Hiking_SAC5-VSHRP.brf']
task :Hiking_SAC6 => ['Hiking_SAC6.brf', 'Hiking_SAC6-SHRP.brf', 'Hiking_SAC6-VSHRP.brf']

CLOBBER.include(Rake::Task[:Walking].prerequisites)
CLOBBER.include(Rake::Task[:Hiking_SAC2].prerequisites)
CLOBBER.include(Rake::Task[:Hiking_SAC3].prerequisites)
CLOBBER.include(Rake::Task[:Hiking_SAC4].prerequisites)
CLOBBER.include(Rake::Task[:Hiking_SAC5].prerequisites)
CLOBBER.include(Rake::Task[:Hiking_SAC6].prerequisites)

rule '.brf' => ['.json'] do |t| 
  sh "mustache #{t.source} Hiking.mustache > #{t.name}"
  File.open(t.source, 'r') do |f|
    puts JSON.load(f)["description"]
  end
end

# FIXME add json files to CLEAN/CLOBBER
# Walking-wet.json -> Walking.json, wet.json
rule( /-.*\.json$/ => [
  proc { |tn| [tn.sub(/-.*.json$/, '.json'), tn.sub(/^.*-/, '')] }
]) do |t|
  puts "Merging #{t.prerequisites.join(', ')} -> #{t.name}"
  # Merge all prerequisites (last file wins)
  config = t.prerequisites.map do |filename|
    JSON.load(File.open(filename))
  end.reduce do |memo, obj|
    memo.merge(obj)
  end
  File.open(t.name, 'w') do |f|
    JSON.dump(config, f)
  end
end
