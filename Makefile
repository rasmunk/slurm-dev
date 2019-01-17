.PHONY: help

OWNER:=nielsbohr
TAG:=edge

ALL_IMAGES:=slurmctld \
	slurmd

# Inspired by https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@echo "slurm-dev images"
	@echo "========================="
	@echo "Replace % with a directory name (e.g., make build/slurmctld)"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build/%:
	docker build --rm --force-rm -t $(OWNER)/$(notdir $@):$(TAG) ./$(notdir $@)

build-all: $(foreach i,$(ALL_IMAGES),build/$(i))

push/%:
	docker push $(OWNER)/$(notdir $@):$(TAG)

push-all: $(foreach i, $(ALL_IMAGES),build/$(i) push/$(i))