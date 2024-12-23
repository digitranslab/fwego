{{/*
Expand the name of the chart.
*/}}
{{- define "fwego.global.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "fwego.global.fullname" -}}
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
{{- define "fwego.global.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "fwego.global.labels" -}}
helm.sh/chart: {{ include "fwego.global.chart" . }}
{{ include "fwego.global.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "fwego.global.selectorLabels" -}}
app.kubernetes.io/name: {{ include "fwego.global.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create image url to use
*/}}
{{- define "fwego.global.image" -}}
{{- if and .Values.global.fwego.imageRegistry .Values.global.fwego.image.tag -}}
{{- printf "%s/%s:%s" .Values.global.fwego.imageRegistry .Values.image.repository .Values.global.fwego.image.tag }}
{{- else -}}
{{- printf "%s:%s" .Values.image.repository .Values.image.tag }}
{{- end }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "fwego.global.serviceAccountName" -}}
{{- if .Values.global.fwego.serviceAccount.create }}
{{- default (include "fwego.global.fullname" .) .Values.global.fwego.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.global.fwego.serviceAccount.name }}
{{- end }}
{{- end }}


{{/*
Create image url to use
*/}}
{{- define "fwego.global.migration.image" -}}
{{- if and .Values.global.fwego.imageRegistry .Values.global.fwego.image.tag -}}
{{- printf "%s/%s:%s" .Values.global.fwego.imageRegistry .Values.migration.image.repository .Values.global.fwego.image.tag }}
{{- else -}}
{{- printf "%s:%s" .Values.migration.image.repository .Chart.AppVersion }}
{{- end }}
{{- end }}

{{/*
Returns the available value for certain key in an existing secret (if it exists),
otherwise it generates a random value.
*/}}
{{- define "getValueFromSecret" }}
{{- $len := (default 16 .Length) | int -}}
{{- $obj := (lookup "v1" "Secret" .Namespace .Name).data -}}
{{- if $obj }}
{{- index $obj .Key | b64dec -}}
{{- else -}}
{{- randAlphaNum $len -}}
{{- end -}}
{{- end }}

{{/*
Get jwt secret name
*/}}
{{- define "fwego.global.jwt.secret_name" -}}
{{- printf "%s%s" (include "fwego.global.fullname" .) "-jwt"  -}}
{{- end }}

{{/*
Get jwt secret key
*/}}
{{- define "fwego.global.jwt.secret_key" -}}
{{- include "getValueFromSecret" (dict "Namespace" .Release.Namespace "Name" .Values.global.fwego.backendSecret "Length" 10 "Key" "SECRET_KEY")  -}}
{{- end }}


{{/*
Get jwt secret key
*/}}
{{- define "fwego.global.jwt.signing_key" -}}
{{- include "getValueFromSecret" (dict "Namespace" .Release.Namespace "Name" .Values.global.fwego.backendSecret "Length" 10 "Key" "FWEGO_JWT_SIGNING_KEY")  -}}
{{- end }}

{{/*
Create envFrom options
*/}}
{{- define "fwego.global.migration.envFrom" -}}
- configMapRef:
    name: {{ .Values.global.fwego.sharedConfigMap }}
- configMapRef:
    name: {{ .Values.global.fwego.backendConfigMap }}
- secretRef:
    name: {{ .Values.global.fwego.backendSecret }}
{{- if .Values.global.fwego.envFrom }}
{{ toYaml .Values.global.fwego.envFrom }}
{{- end }}
{{- if .Values.migration.envFrom }}
{{ toYaml .Values.migration.envFrom }}
{{- end }}
{{- end }}

{{/*
Get the password for the postgresql user
*/}}
{{- define "fwego.global.postgresql.password" -}}
  {{- if .Values.postgresql.enabled -}}
  {{- if .Values.postgresql.auth.existingSecret -}}
    {{- include "getValueFromSecret" (dict "Namespace" (include "common.names.namespace" .Subcharts.postgresq) "Name" (include "postgresql.v1.secretName" .Subcharts.postgresq) "Length" 10 "Key" (include "postgresql.v1.userPasswordKey" .Subcharts.postgresq))  -}}
  {{- else if .Values.postgresql.auth.password -}}
    {{ .Values.postgresql.auth.password }}
  {{- end -}}
  {{- end -}}
{{- end -}}

{{/*
Return the username for the postgres user
*/}}
{{- define "fwego.global.postgresql.username" -}}
  {{- if .Values.postgresql.enabled -}}
    {{ include "postgresql.v1.username" .Subcharts.postgresql }}
  {{- end -}}
{{- end -}}

{{/*
PodSecurityContext combine the global and local PodSecurityContexts
*/}}
{{- define "podSecurityContext" -}}
{{- if .Values.migration.securityContext.enabled }}
{{- omit .Values.migration.securityContext "enabled" | toYaml  }}
{{- else if .Values.global.fwego.securityContext.enabled }}
{{- omit .Values.global.fwego.securityContext "enabled" | toYaml }}
{{- end }}
{{- end }}

{{/*
ContainerSecurityContext combine the global and local ContainerSecurityContexts
*/}}
{{- define "containerSecurityContext" -}}
{{- if .Values.migration.containerSecurityContext.enabled }}
{{- omit .Values.migration.containerSecurityContext "enabled" | toYaml  }}
{{- else if .Values.global.fwego.containerSecurityContext.enabled }}
{{- omit .Values.global.fwego.containerSecurityContext "enabled" | toYaml }}
{{- end }}
{{- end }}
