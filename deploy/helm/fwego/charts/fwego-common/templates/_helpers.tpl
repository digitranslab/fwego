{{/*
Expand the name of the chart.
*/}}
{{- define "fwego.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Expand the namespace of the chart.
*/}}
{{- define "fwego.namespace" -}}
{{- default .Release.Namespace .Values.namespace }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "fwego.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "fwego.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "fwego.additionalLabels" }}
{{- range $key, $val := .Values.additionalLabels }}
{{ $key }}: {{ $val }}
{{- end }}
{{- end }}

{{- define "fwego.additionalSelectorLabels" }}
{{- range $key, $val := .Values.additionalSelectorLabels }}
{{ $key }}: {{ $val }}
{{- end }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "fwego.labels" -}}
helm.sh/chart: {{ include "fwego.chart" . }}
{{ include "fwego.selectorLabels" . }}
{{ include "fwego.additionalLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "fwego.selectorLabels" -}}
app.kubernetes.io/name: {{ include "fwego.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{ include "fwego.additionalSelectorLabels" . }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "fwego.serviceAccountName" -}}
{{- if not .Values.global.fwego.serviceAccount.shared -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "fwego.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{ else }}
{{- default "default" .Values.global.fwego.serviceAccount.name }}
{{- end }}
{{- end }}


{{/*
Create command for readiness probe
*/}}
{{- define "fwego.readinessProbeCommand" -}}
{{- $command := .Values.readinessProbe.command }}
{{- if $command }}
{{- printf "command:" | nindent 4 -}}
{{- toYaml $command | nindent 6 -}}
{{ else }}
{{- printf "command:" | nindent 4 -}}
{{- printf "- /bin/bash" | nindent 6 -}}
{{- printf "- -c" | nindent 6 -}}
{{- printf "- /fwego/backend/docker/docker-entrypoint.sh backend-healthcheck" | nindent 6 -}}
{{- end }}
{{- end }}

{{/*
Create full readinessProbe
*/}}
{{- define "fwego.readinessProbe" -}}
{{- if .Values.readinessProbe }}
readinessProbe:
  exec: {{ include "fwego.readinessProbeCommand" . }}
  initialDelaySeconds: {{ .Values.readinessProbe.initialDelaySeconds }}
  periodSeconds: {{ .Values.readinessProbe.periodSeconds }}
  timeoutSeconds: {{ .Values.readinessProbe.timeoutSeconds }}
  successThreshold: {{ .Values.readinessProbe.successThreshold }}
  failureThreshold: {{ .Values.readinessProbe.failureThreshold }}
{{- end }}
{{- end }}

{{/*
Create command for liveness probe
*/}}
{{- define "fwego.livenessProbeCommand" -}}
{{- $command := .Values.livenessProbe.command }}
{{- if $command }}
{{- printf "command:" | nindent 4 -}}
{{- toYaml $command | nindent 6 -}}
{{ else }}
{{- printf "command:" | nindent 4 -}}
{{- printf "- /bin/bash" | nindent 6 -}}
{{- printf "- -c" | nindent 6 -}}
{{- printf "- /fwego/backend/docker/docker-entrypoint.sh backend-healthcheck" | nindent 6 -}}
{{- end }}
{{- end }}

{{/*
Create full livenessProbe
*/}}
{{- define "fwego.livenessProbe" -}}
{{- if .Values.livenessProbe }}
livenessProbe:
  exec: {{ include "fwego.livenessProbeCommand" . }}
  initialDelaySeconds: {{ .Values.livenessProbe.initialDelaySeconds }}
  periodSeconds: {{ .Values.livenessProbe.periodSeconds }}
  timeoutSeconds: {{ .Values.livenessProbe.timeoutSeconds }}
  successThreshold: {{ .Values.livenessProbe.successThreshold }}
  failureThreshold: {{ .Values.livenessProbe.failureThreshold }}
{{- end }}
{{- end }}

{{/*
Image Pull secrets combine the global and local imagePullSecrets
*/}}
{{- define "fwego.imagePullSecrets" -}}
{{- $global := .Values.global.fwego.imagePullSecrets }}
{{- $local := .Values.imagePullSecrets }}
{{- if and $global $local }}
{{- $all := concat $global $local -}}
{{- toYaml $all | nindent 8}}
{{- else if $global }}
{{- toYaml $global | nindent 8}}
{{- else if $local }}
{{- toYaml $local | nindent 8}}
{{- end }}
{{- end }}

{{/*
Create image url to use
*/}}
{{- define "fwego.image" -}}
{{- if and .Values.global.fwego.imageRegistry .Values.global.fwego.image.tag -}}
{{- printf "%s/%s:%s" .Values.global.fwego.imageRegistry .Values.image.repository .Values.global.fwego.image.tag }}
{{- else -}}
{{- printf "%s:%s" .Values.image.repository .Values.image.tag }}
{{- end }}
{{- end }}

{{/*
Create envFrom options
*/}}
{{- define "fwego.envFrom" -}}
{{- if .Values.mountConfiguration.backend }}
- configMapRef:
    name: {{ .Values.global.fwego.sharedConfigMap }}
- configMapRef:
    name: {{ .Values.global.fwego.backendConfigMap }}
- secretRef:
    name: {{ .Values.global.fwego.backendSecret }}
{{ end }}
{{- if .Values.mountConfiguration.frontend }}
- configMapRef:
    name: {{ .Values.global.fwego.sharedConfigMap }}
- configMapRef:
    name: {{ .Values.global.fwego.frontendConfigMap }}
{{ end }}
{{- if .Values.global.fwego.envFrom }}
{{ toYaml .Values.global.fwego.envFrom }}
{{- end }}
{{- if .Values.envFrom }}
{{ toYaml .Values.envFrom }}
{{- end }}
{{- end }}

{{/*
PodSecurityContext combine the global and local PodSecurityContexts
*/}}
{{- define "fwego.podSecurityContext" -}}
{{- if .Values.securityContext.enabled }}
{{- omit .Values.securityContext "enabled" | toYaml  }}
{{- else if .Values.global.fwego.securityContext.enabled }}
{{- omit .Values.global.fwego.securityContext "enabled" | toYaml }}
{{- end }}
{{- end }}

{{/*
ContainerSecurityContext combine the global and local ContainerSecurityContexts
*/}}
{{- define "fwego.containerSecurityContext" -}}
{{- if .Values.containerSecurityContext.enabled }}
{{- omit .Values.containerSecurityContext "enabled" | toYaml  }}
{{- else if .Values.global.fwego.containerSecurityContext.enabled }}
{{- omit .Values.global.fwego.containerSecurityContext "enabled" | toYaml }}
{{- end }}
{{- end }}
